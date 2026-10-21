# EMA Hourly Continuation — XEC/USDT P34_144

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.6094 |
| sortino_ratio | -0.4688 |
| max_drawdown | 0.5021 |
| cagr | -0.1947 |
| net_avg_win | 70.9220 |
| net_avg_loss | -92.3880 |
| avg_hold_time_bars | 22.2193 |
| exposure | 0.4173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
