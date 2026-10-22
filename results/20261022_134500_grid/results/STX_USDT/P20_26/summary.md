# EMA Hourly Continuation — STX/USDT P20_26

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.2743 |
| net_win_rate | 0.3814 |
| gross_profit_factor | 0.7228 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -13.1250 |
| sortino_ratio | -6.4696 |
| max_drawdown | 0.9998 |
| cagr | -0.9668 |
| net_avg_win | 8.4531 |
| net_avg_loss | -19.0023 |
| avg_hold_time_bars | 2.0043 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
