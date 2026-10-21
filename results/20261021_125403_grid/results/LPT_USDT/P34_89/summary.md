# EMA Hourly Continuation — LPT/USDT P34_89

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.9961 |
| sortino_ratio | -0.9337 |
| max_drawdown | 0.6678 |
| cagr | -0.3505 |
| net_avg_win | 60.4693 |
| net_avg_loss | -76.6139 |
| avg_hold_time_bars | 10.0125 |
| exposure | 0.2185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
