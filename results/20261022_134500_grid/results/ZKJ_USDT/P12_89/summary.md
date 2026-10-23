# EMA Hourly Continuation — ZKJ/USDT P12_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.1931 |
| net_win_rate | 0.3104 |
| gross_profit_factor | 0.4738 |
| gross_win_rate | 0.3659 |
| sharpe_ratio | -10.0203 |
| sortino_ratio | -3.1678 |
| max_drawdown | 0.9879 |
| cagr | -0.8252 |
| net_avg_win | 16.8843 |
| net_avg_loss | -39.3522 |
| avg_hold_time_bars | 38.6962 |
| exposure | 0.7933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
