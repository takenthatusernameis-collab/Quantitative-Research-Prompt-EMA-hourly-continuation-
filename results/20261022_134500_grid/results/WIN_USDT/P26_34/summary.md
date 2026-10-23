# EMA Hourly Continuation — WIN/USDT P26_34

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.1353 |
| net_win_rate | 0.3116 |
| gross_profit_factor | 0.6360 |
| gross_win_rate | 0.3688 |
| sharpe_ratio | -15.7257 |
| sortino_ratio | -7.5519 |
| max_drawdown | 1.0000 |
| cagr | -0.9836 |
| net_avg_win | 5.0485 |
| net_avg_loss | -16.8828 |
| avg_hold_time_bars | 2.1739 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
