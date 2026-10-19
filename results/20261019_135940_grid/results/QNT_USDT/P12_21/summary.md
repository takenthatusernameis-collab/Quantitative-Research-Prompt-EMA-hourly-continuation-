# EMA Hourly Continuation — QNT/USDT P12_21

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1563 |
| net_profit_factor | 0.1673 |
| net_win_rate | 0.3756 |
| gross_profit_factor | 0.5915 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -15.6567 |
| sortino_ratio | -8.9769 |
| max_drawdown | 1.0000 |
| cagr | -0.9906 |
| net_avg_win | 3.4224 |
| net_avg_loss | -12.3042 |
| avg_hold_time_bars | 2.2182 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
