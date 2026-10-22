# EMA Hourly Continuation — BTT/USDT P20_26

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1271 |
| net_profit_factor | 0.1024 |
| net_win_rate | 0.2242 |
| gross_profit_factor | 0.5434 |
| gross_win_rate | 0.3430 |
| sharpe_ratio | -21.5112 |
| sortino_ratio | -12.4514 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 4.0039 |
| net_avg_loss | -11.2993 |
| avg_hold_time_bars | 2.1511 |
| exposure | 0.1243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
