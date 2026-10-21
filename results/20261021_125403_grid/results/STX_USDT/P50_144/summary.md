# EMA Hourly Continuation — STX/USDT P50_144

**Symbol:** STX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.3243 |
| sortino_ratio | -0.3460 |
| max_drawdown | 0.3607 |
| cagr | -0.1475 |
| net_avg_win | 70.2613 |
| net_avg_loss | -89.5679 |
| avg_hold_time_bars | 18.6119 |
| exposure | 0.2821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
