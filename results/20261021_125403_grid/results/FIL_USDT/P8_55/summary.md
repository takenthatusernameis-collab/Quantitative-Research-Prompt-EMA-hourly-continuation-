# EMA Hourly Continuation — FIL/USDT P8_55

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.8330 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.4555 |
| sortino_ratio | -0.5160 |
| max_drawdown | 0.4835 |
| cagr | -0.2132 |
| net_avg_win | 72.3233 |
| net_avg_loss | -91.2078 |
| avg_hold_time_bars | 17.1182 |
| exposure | 0.4739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
