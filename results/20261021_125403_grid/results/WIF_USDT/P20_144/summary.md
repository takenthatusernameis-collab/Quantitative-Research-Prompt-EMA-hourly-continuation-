# EMA Hourly Continuation — WIF/USDT P20_144

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7697 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -1.5152 |
| sortino_ratio | -0.4027 |
| max_drawdown | 0.3874 |
| cagr | -0.1709 |
| net_avg_win | 76.0317 |
| net_avg_loss | -88.1030 |
| avg_hold_time_bars | 34.4114 |
| exposure | 0.5475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
