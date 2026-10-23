# EMA Hourly Continuation — SLP/USDT P21_144

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -3.4258 |
| sortino_ratio | -1.1691 |
| max_drawdown | 0.7611 |
| cagr | -0.4295 |
| net_avg_win | 53.4202 |
| net_avg_loss | -73.6851 |
| avg_hold_time_bars | 19.9253 |
| exposure | 0.5335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
