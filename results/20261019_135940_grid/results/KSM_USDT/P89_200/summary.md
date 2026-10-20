# EMA Hourly Continuation — KSM/USDT P89_200

**Symbol:** KSM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6505 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0887 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -2.7009 |
| sortino_ratio | -0.7553 |
| max_drawdown | 0.6230 |
| cagr | -0.3036 |
| net_avg_win | 56.3872 |
| net_avg_loss | -87.5760 |
| avg_hold_time_bars | 10.7577 |
| exposure | 0.1917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
