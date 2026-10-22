# EMA Hourly Continuation — LINK/USDT P34_144

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6446 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0635 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -3.0938 |
| sortino_ratio | -0.9581 |
| max_drawdown | 0.7064 |
| cagr | -0.3740 |
| net_avg_win | 50.7977 |
| net_avg_loss | -79.4424 |
| avg_hold_time_bars | 16.5874 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
