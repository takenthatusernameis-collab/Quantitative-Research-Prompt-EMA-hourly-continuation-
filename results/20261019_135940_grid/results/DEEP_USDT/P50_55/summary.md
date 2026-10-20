# EMA Hourly Continuation — DEEP/USDT P50_55

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.3886 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.8113 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -9.0628 |
| sortino_ratio | -3.4966 |
| max_drawdown | 0.9766 |
| cagr | -0.8435 |
| net_avg_win | 25.4324 |
| net_avg_loss | -46.0165 |
| avg_hold_time_bars | 1.8866 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
