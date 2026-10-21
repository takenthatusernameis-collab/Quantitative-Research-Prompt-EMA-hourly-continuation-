# EMA Hourly Continuation — WIF/USDT P12_21

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.9372 |
| net_win_rate | 0.5447 |
| gross_profit_factor | 1.1925 |
| gross_win_rate | 0.5447 |
| sharpe_ratio | -0.3132 |
| sortino_ratio | -0.0696 |
| max_drawdown | 0.2700 |
| cagr | -0.0343 |
| net_avg_win | 97.8119 |
| net_avg_loss | -124.8495 |
| avg_hold_time_bars | 4.9660 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
