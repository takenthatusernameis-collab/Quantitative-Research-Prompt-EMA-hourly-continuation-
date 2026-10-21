# EMA Hourly Continuation — ORCA/USDT P8_55

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.8194 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.7076 |
| sortino_ratio | -0.6673 |
| max_drawdown | 0.5836 |
| cagr | -0.2670 |
| net_avg_win | 64.5262 |
| net_avg_loss | -83.1059 |
| avg_hold_time_bars | 13.7857 |
| exposure | 0.4650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
