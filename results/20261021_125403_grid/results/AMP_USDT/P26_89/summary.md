# EMA Hourly Continuation — AMP/USDT P26_89

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.5333 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7143 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -4.5183 |
| sortino_ratio | -1.4763 |
| max_drawdown | 0.8266 |
| cagr | -0.4940 |
| net_avg_win | 42.1784 |
| net_avg_loss | -56.6338 |
| avg_hold_time_bars | 12.5226 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
