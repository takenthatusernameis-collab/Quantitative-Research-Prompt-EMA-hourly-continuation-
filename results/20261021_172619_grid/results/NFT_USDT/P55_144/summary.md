# EMA Hourly Continuation — NFT/USDT P55_144

**Symbol:** NFT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.3787 |
| net_win_rate | 0.3418 |
| gross_profit_factor | 0.6521 |
| gross_win_rate | 0.3446 |
| sharpe_ratio | -6.5769 |
| sortino_ratio | -1.7940 |
| max_drawdown | 0.8829 |
| cagr | -0.5701 |
| net_avg_win | 44.3376 |
| net_avg_loss | -60.7932 |
| avg_hold_time_bars | 15.8136 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
