# EMA Hourly Continuation — XPR/USDT P12_144

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7910 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.3964 |
| sortino_ratio | -0.3907 |
| max_drawdown | 0.4206 |
| cagr | -0.1652 |
| net_avg_win | 72.6332 |
| net_avg_loss | -89.9278 |
| avg_hold_time_bars | 32.7656 |
| exposure | 0.5719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
