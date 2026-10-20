# EMA Hourly Continuation — XCH/USDT P20_144

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6100 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.5899 |
| sortino_ratio | -1.2764 |
| max_drawdown | 0.7958 |
| cagr | -0.4623 |
| net_avg_win | 39.9657 |
| net_avg_loss | -60.0719 |
| avg_hold_time_bars | 18.2307 |
| exposure | 0.5353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
