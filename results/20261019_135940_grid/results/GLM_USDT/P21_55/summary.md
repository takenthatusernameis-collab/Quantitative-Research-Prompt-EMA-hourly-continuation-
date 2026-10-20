# EMA Hourly Continuation — GLM/USDT P21_55

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.4336 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.7634 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -6.7741 |
| sortino_ratio | -2.8326 |
| max_drawdown | 0.9673 |
| cagr | -0.7431 |
| net_avg_win | 18.8844 |
| net_avg_loss | -35.6436 |
| avg_hold_time_bars | 6.5075 |
| exposure | 0.2576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
