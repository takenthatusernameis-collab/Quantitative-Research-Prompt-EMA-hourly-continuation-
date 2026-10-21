# EMA Hourly Continuation — CFX/USDT P12_34

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7596 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0147 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.0837 |
| sortino_ratio | -0.7002 |
| max_drawdown | 0.6055 |
| cagr | -0.2739 |
| net_avg_win | 63.2291 |
| net_avg_loss | -84.7806 |
| avg_hold_time_bars | 7.5027 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
