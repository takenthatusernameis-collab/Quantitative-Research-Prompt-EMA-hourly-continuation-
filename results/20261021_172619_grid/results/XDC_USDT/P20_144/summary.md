# EMA Hourly Continuation — XDC/USDT P20_144

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7780 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.5688 |
| sortino_ratio | -0.4757 |
| max_drawdown | 0.4285 |
| cagr | -0.1968 |
| net_avg_win | 64.2180 |
| net_avg_loss | -88.2718 |
| avg_hold_time_bars | 21.1588 |
| exposure | 0.4299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
