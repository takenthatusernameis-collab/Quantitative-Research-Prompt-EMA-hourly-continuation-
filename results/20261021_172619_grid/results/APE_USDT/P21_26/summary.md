# EMA Hourly Continuation — APE/USDT P21_26

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 149 |
| net_profit_factor | 0.6623 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9030 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -1.5420 |
| sortino_ratio | -0.2694 |
| max_drawdown | 0.2844 |
| cagr | -0.1163 |
| net_avg_win | 73.7254 |
| net_avg_loss | -101.3233 |
| avg_hold_time_bars | 3.8591 |
| exposure | 0.0261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
