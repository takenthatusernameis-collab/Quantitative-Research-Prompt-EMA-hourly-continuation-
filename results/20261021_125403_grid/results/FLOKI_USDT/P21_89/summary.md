# EMA Hourly Continuation — FLOKI/USDT P21_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7751 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.7817 |
| sortino_ratio | -0.5682 |
| max_drawdown | 0.5121 |
| cagr | -0.2304 |
| net_avg_win | 68.0655 |
| net_avg_loss | -84.3616 |
| avg_hold_time_bars | 17.0783 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
