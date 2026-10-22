# EMA Hourly Continuation — HTX/USDT P8_89

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 785 |
| net_profit_factor | 0.3150 |
| net_win_rate | 0.3376 |
| gross_profit_factor | 0.7183 |
| gross_win_rate | 0.3898 |
| sharpe_ratio | -11.3843 |
| sortino_ratio | -4.5876 |
| max_drawdown | 0.9981 |
| cagr | -0.9169 |
| net_avg_win | 17.3214 |
| net_avg_loss | -28.0218 |
| avg_hold_time_bars | 18.0382 |
| exposure | 0.6408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
