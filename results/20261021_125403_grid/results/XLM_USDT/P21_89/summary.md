# EMA Hourly Continuation — XLM/USDT P21_89

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1232 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -1.2550 |
| sortino_ratio | -0.3882 |
| max_drawdown | 0.4069 |
| cagr | -0.1641 |
| net_avg_win | 63.5375 |
| net_avg_loss | -88.9672 |
| avg_hold_time_bars | 18.5316 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
