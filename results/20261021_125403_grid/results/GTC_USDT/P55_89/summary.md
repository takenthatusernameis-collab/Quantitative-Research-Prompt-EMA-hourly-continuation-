# EMA Hourly Continuation — GTC/USDT P55_89

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6616 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.7002 |
| sortino_ratio | -0.7621 |
| max_drawdown | 0.6073 |
| cagr | -0.2961 |
| net_avg_win | 61.9298 |
| net_avg_loss | -83.6558 |
| avg_hold_time_bars | 7.0561 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
