# EMA Hourly Continuation — ZRO/USDT P21_144

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -1.3132 |
| sortino_ratio | -0.3627 |
| max_drawdown | 0.3480 |
| cagr | -0.1552 |
| net_avg_win | 75.7511 |
| net_avg_loss | -88.2748 |
| avg_hold_time_bars | 31.1175 |
| exposure | 0.5315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
