# EMA Hourly Continuation — DEGEN/USDT P12_34

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9761 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -6.1624 |
| sortino_ratio | -2.9999 |
| max_drawdown | 0.9755 |
| cagr | -0.7634 |
| net_avg_win | 31.5149 |
| net_avg_loss | -42.9992 |
| avg_hold_time_bars | 4.7866 |
| exposure | 0.2604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
