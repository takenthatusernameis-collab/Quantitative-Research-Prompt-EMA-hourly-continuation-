# EMA Hourly Continuation — ETHFI/USDT P12_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7020 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.9124 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -2.8742 |
| sortino_ratio | -0.8980 |
| max_drawdown | 0.6666 |
| cagr | -0.3446 |
| net_avg_win | 67.8709 |
| net_avg_loss | -82.8165 |
| avg_hold_time_bars | 30.5244 |
| exposure | 0.6826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
