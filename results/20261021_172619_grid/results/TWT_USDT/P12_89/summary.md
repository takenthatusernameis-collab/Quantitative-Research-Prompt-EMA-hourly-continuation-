# EMA Hourly Continuation — TWT/USDT P12_89

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.9870 |
| sortino_ratio | -0.6916 |
| max_drawdown | 0.5906 |
| cagr | -0.2732 |
| net_avg_win | 62.6826 |
| net_avg_loss | -83.1324 |
| avg_hold_time_bars | 19.5178 |
| exposure | 0.5225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
