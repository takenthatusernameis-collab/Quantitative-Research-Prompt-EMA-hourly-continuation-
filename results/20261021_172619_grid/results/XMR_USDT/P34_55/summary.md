# EMA Hourly Continuation — XMR/USDT P34_55

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.4631 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.6596 |
| gross_win_rate | 0.3883 |
| sharpe_ratio | -3.4742 |
| sortino_ratio | -0.7086 |
| max_drawdown | 0.5649 |
| cagr | -0.2782 |
| net_avg_win | 60.2725 |
| net_avg_loss | -82.6336 |
| avg_hold_time_bars | 5.2864 |
| exposure | 0.0495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
