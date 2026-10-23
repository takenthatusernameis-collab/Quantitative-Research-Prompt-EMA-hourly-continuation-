# EMA Hourly Continuation — GMX/USDT P8_89

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -4.3339 |
| sortino_ratio | -1.6858 |
| max_drawdown | 0.8661 |
| cagr | -0.5483 |
| net_avg_win | 38.6495 |
| net_avg_loss | -54.8071 |
| avg_hold_time_bars | 17.8558 |
| exposure | 0.6193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
