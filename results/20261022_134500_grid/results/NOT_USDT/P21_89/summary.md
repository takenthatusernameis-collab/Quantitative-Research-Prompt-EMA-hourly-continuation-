# EMA Hourly Continuation — NOT/USDT P21_89

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.5977 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.6205 |
| sortino_ratio | -1.7798 |
| max_drawdown | 0.8837 |
| cagr | -0.5781 |
| net_avg_win | 37.8826 |
| net_avg_loss | -56.3404 |
| avg_hold_time_bars | 10.5048 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
