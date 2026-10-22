# EMA Hourly Continuation — TRX/USDT P26_200

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.3216 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -6.0623 |
| sortino_ratio | -1.7056 |
| max_drawdown | 0.8958 |
| cagr | -0.5907 |
| net_avg_win | 25.3745 |
| net_avg_loss | -56.5517 |
| avg_hold_time_bars | 28.4050 |
| exposure | 0.5165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
