# EMA Hourly Continuation — RUNE/USDT P50_200

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 1.0682 |
| net_win_rate | 0.5661 |
| gross_profit_factor | 1.3055 |
| gross_win_rate | 0.5661 |
| sharpe_ratio | 0.3596 |
| sortino_ratio | 0.0817 |
| max_drawdown | 0.1788 |
| cagr | 0.0308 |
| net_avg_win | 90.4670 |
| net_avg_loss | -110.4989 |
| avg_hold_time_bars | 44.3430 |
| exposure | 0.4878 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
