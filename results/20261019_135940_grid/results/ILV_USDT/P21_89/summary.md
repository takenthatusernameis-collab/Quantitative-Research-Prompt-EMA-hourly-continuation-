# EMA Hourly Continuation — ILV/USDT P21_89

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 1.0165 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -3.7256 |
| sortino_ratio | -1.4273 |
| max_drawdown | 0.8177 |
| cagr | -0.4866 |
| net_avg_win | 47.8198 |
| net_avg_loss | -67.9183 |
| avg_hold_time_bars | 10.9231 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
