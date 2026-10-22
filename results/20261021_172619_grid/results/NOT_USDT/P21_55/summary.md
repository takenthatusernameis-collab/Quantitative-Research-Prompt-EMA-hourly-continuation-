# EMA Hourly Continuation — NOT/USDT P21_55

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.8318 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.2137 |
| sortino_ratio | -0.3866 |
| max_drawdown | 0.3997 |
| cagr | -0.1644 |
| net_avg_win | 71.3897 |
| net_avg_loss | -91.8193 |
| avg_hold_time_bars | 7.6962 |
| exposure | 0.1714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
