# EMA Hourly Continuation — ETH/USDT P26_89

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6856 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.2602 |
| sortino_ratio | -0.6186 |
| max_drawdown | 0.5276 |
| cagr | -0.2467 |
| net_avg_win | 61.3331 |
| net_avg_loss | -88.0033 |
| avg_hold_time_bars | 19.2411 |
| exposure | 0.3192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
