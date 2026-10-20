# EMA Hourly Continuation — TFUEL/USDT P20_34

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.3467 |
| net_win_rate | 0.3609 |
| gross_profit_factor | 0.8346 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -13.3851 |
| sortino_ratio | -6.7214 |
| max_drawdown | 0.9999 |
| cagr | -0.9696 |
| net_avg_win | 11.9228 |
| net_avg_loss | -19.4215 |
| avg_hold_time_bars | 3.1963 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
