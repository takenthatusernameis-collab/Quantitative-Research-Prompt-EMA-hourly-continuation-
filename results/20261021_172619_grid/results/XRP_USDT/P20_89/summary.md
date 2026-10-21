# EMA Hourly Continuation — XRP/USDT P20_89

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6881 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.4725 |
| sortino_ratio | -0.7631 |
| max_drawdown | 0.6263 |
| cagr | -0.2944 |
| net_avg_win | 56.2086 |
| net_avg_loss | -79.6009 |
| avg_hold_time_bars | 15.8211 |
| exposure | 0.3337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
