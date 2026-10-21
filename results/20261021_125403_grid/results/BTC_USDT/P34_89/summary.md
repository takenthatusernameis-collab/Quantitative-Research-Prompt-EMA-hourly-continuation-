# EMA Hourly Continuation — BTC/USDT P34_89

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5596 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.3084 |
| sortino_ratio | -0.9335 |
| max_drawdown | 0.7064 |
| cagr | -0.3475 |
| net_avg_win | 41.4332 |
| net_avg_loss | -72.6926 |
| avg_hold_time_bars | 13.2317 |
| exposure | 0.2308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
