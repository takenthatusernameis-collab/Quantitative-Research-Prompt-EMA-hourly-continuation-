# EMA Hourly Continuation — ATH/USDT P21_200

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8919 |
| net_win_rate | 0.5490 |
| gross_profit_factor | 1.2214 |
| gross_win_rate | 0.5515 |
| sharpe_ratio | -0.7216 |
| sortino_ratio | -0.2076 |
| max_drawdown | 0.2989 |
| cagr | -0.0988 |
| net_avg_win | 84.2025 |
| net_avg_loss | -114.9029 |
| avg_hold_time_bars | 31.6959 |
| exposure | 0.5961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
