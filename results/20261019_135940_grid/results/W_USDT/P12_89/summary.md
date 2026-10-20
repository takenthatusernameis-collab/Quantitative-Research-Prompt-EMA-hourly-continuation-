# EMA Hourly Continuation — W/USDT P12_89

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0480 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -2.3532 |
| sortino_ratio | -0.8567 |
| max_drawdown | 0.6844 |
| cagr | -0.3375 |
| net_avg_win | 53.2164 |
| net_avg_loss | -76.1550 |
| avg_hold_time_bars | 18.3453 |
| exposure | 0.5579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
