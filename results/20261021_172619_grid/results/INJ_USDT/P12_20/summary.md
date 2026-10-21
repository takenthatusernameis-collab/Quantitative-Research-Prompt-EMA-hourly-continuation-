# EMA Hourly Continuation — INJ/USDT P12_20

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5228 |
| gross_profit_factor | 1.0846 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -0.9537 |
| sortino_ratio | -0.2135 |
| max_drawdown | 0.2636 |
| cagr | -0.0940 |
| net_avg_win | 76.9935 |
| net_avg_loss | -103.4587 |
| avg_hold_time_bars | 6.2282 |
| exposure | 0.0682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
