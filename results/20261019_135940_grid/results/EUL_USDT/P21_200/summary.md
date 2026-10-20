# EMA Hourly Continuation — EUL/USDT P21_200

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6131 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8160 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -2.8010 |
| sortino_ratio | -0.7972 |
| max_drawdown | 0.6280 |
| cagr | -0.3138 |
| net_avg_win | 51.8207 |
| net_avg_loss | -71.1979 |
| avg_hold_time_bars | 30.0538 |
| exposure | 0.5587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
