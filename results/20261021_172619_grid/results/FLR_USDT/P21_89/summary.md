# EMA Hourly Continuation — FLR/USDT P21_89

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.7966 |
| sortino_ratio | -0.9164 |
| max_drawdown | 0.6732 |
| cagr | -0.3434 |
| net_avg_win | 57.1590 |
| net_avg_loss | -74.8676 |
| avg_hold_time_bars | 13.8182 |
| exposure | 0.3316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
