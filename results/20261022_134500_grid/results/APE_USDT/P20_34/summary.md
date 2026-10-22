# EMA Hourly Continuation — APE/USDT P20_34

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.2874 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.6860 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -11.0623 |
| sortino_ratio | -5.3470 |
| max_drawdown | 0.9989 |
| cagr | -0.9337 |
| net_avg_win | 8.5909 |
| net_avg_loss | -20.3752 |
| avg_hold_time_bars | 2.3276 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
