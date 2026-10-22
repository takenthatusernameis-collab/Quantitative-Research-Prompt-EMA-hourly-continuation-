# EMA Hourly Continuation — LDO/USDT P34_144

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6121 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -3.7867 |
| sortino_ratio | -1.2019 |
| max_drawdown | 0.7628 |
| cagr | -0.4297 |
| net_avg_win | 53.4936 |
| net_avg_loss | -69.1094 |
| avg_hold_time_bars | 16.8416 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
