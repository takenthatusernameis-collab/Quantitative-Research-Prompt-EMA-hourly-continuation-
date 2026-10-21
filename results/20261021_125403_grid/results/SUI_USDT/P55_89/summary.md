# EMA Hourly Continuation — SUI/USDT P55_89

**Symbol:** SUI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8020 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0620 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -1.0844 |
| sortino_ratio | -0.2576 |
| max_drawdown | 0.2938 |
| cagr | -0.1122 |
| net_avg_win | 74.2123 |
| net_avg_loss | -99.5938 |
| avg_hold_time_bars | 6.1618 |
| exposure | 0.0762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
