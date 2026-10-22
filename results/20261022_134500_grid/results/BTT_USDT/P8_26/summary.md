# EMA Hourly Continuation — BTT/USDT P8_26

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1606 |
| net_profit_factor | 0.2409 |
| net_win_rate | 0.3182 |
| gross_profit_factor | 0.6474 |
| gross_win_rate | 0.3829 |
| sharpe_ratio | -19.0174 |
| sortino_ratio | -11.2444 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 6.2112 |
| net_avg_loss | -12.0310 |
| avg_hold_time_bars | 4.1681 |
| exposure | 0.3043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
