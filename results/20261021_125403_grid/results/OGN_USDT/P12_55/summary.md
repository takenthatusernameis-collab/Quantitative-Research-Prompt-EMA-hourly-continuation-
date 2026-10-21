# EMA Hourly Continuation — OGN/USDT P12_55

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7003 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -3.1836 |
| sortino_ratio | -1.1631 |
| max_drawdown | 0.7522 |
| cagr | -0.4136 |
| net_avg_win | 55.0686 |
| net_avg_loss | -71.5653 |
| avg_hold_time_bars | 11.6844 |
| exposure | 0.3484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
