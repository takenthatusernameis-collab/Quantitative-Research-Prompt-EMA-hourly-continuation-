# EMA Hourly Continuation — ETN/USDT P26_89

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.3654 |
| net_win_rate | 0.3600 |
| gross_profit_factor | 0.5629 |
| gross_win_rate | 0.3752 |
| sharpe_ratio | -9.1140 |
| sortino_ratio | -3.7742 |
| max_drawdown | 0.9801 |
| cagr | -0.8443 |
| net_avg_win | 21.6215 |
| net_avg_loss | -33.2814 |
| avg_hold_time_bars | 7.5324 |
| exposure | 0.2966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
