# EMA Hourly Continuation — ILV/USDT P55_200

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7951 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.1293 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -1.3591 |
| sortino_ratio | -0.3529 |
| max_drawdown | 0.3841 |
| cagr | -0.1576 |
| net_avg_win | 76.7364 |
| net_avg_loss | -104.7967 |
| avg_hold_time_bars | 24.9000 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
